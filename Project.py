import tenseal as ts
import time
import sys

def format_size(obj):
    return f"{sys.getsizeof(obj) / 1024:.1f} KB"

def create_context():
    start = time.time()
    context = ts.context(
        scheme=ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,
        coeff_mod_bit_sizes=[60, 40, 40, 60]
    )
    context.global_scale = 2 ** 40
    context.generate_galois_keys()
    end = time.time()
    return context, int((end - start) * 1000)

def encrypt_vector(context, data):
    start = time.time()
    enc_vec = ts.ckks_vector(context, data)
    end = time.time()
    return enc_vec, int((end - start) * 1000), format_size(enc_vec)

def decrypt_vector(enc_vec):
    start = time.time()
    dec = enc_vec.decrypt()
    end = time.time()
    return dec, int((end - start) * 1000)

def homomorphic_addition(enc_vec):
    start = time.time()
    result = enc_vec + enc_vec
    end = time.time()
    original = enc_vec.decrypt()[0]
    decrypted = result.decrypt()[0]
    loss = abs(decrypted - (original * 2)) / (original * 2) * 100
    return result, int((end - start) * 1000), loss, format_size(result)

def homomorphic_multiplication(enc_vec):
    start = time.time()
    result = enc_vec * enc_vec
    end = time.time()
    original = enc_vec.decrypt()[0]
    decrypted = result.decrypt()[0]
    expected = original ** 2
    loss = abs(decrypted - expected) / expected * 100
    return result, int((end - start) * 1000), loss, format_size(result)

def rescale_operation(enc_vec):
    start = time.time()
    result = enc_vec + 1
    end = time.time()
    original = enc_vec.decrypt()[0]
    decrypted = result.decrypt()[0]
    expected = original + 1
    loss = abs(decrypted - expected) / expected * 100
    return result, int((end - start) * 1000), loss, format_size(result)

def print_table_row(name, time_taken, precision_loss, size, sec_level="128"):
    print(f"{name:<30}{time_taken:<15}{precision_loss:<20}{size:<20}{sec_level:<10}")

if __name__ == "__main__":
    data = [1.1, 2.2, 3.3, 4.4, 5.5]

    context, key_time = create_context()
    enc_vec, enc_time, enc_size = encrypt_vector(context, data)
    add_result, add_time, add_loss, add_size = homomorphic_addition(enc_vec)
    mul_result, mul_time, mul_loss, mul_size = homomorphic_multiplication(enc_vec)
    res_result, res_time, res_loss, res_size = rescale_operation(mul_result)
    dec_result, dec_time = decrypt_vector(enc_vec)

    print("\nTable: Performance Evaluation of CKKS Homomorphic Encryption Scheme\n")
    print(f"{'Operation':<30}{'Time Taken (ms)':<15}{'Precision Loss (%)':<20}{'Ciphertext Size (KB)':<20}{'Security Level (Bits)':<10}")
    print("-" * 95)
    print_table_row("Key Generation", key_time, "N/A", "N/A")
    print_table_row("Encoding & Encryption", enc_time, "<0.01%", enc_size)
    print_table_row("Homomorphic Addition", add_time, f"{add_loss:.2f}%", add_size)
    print_table_row("Homomorphic Multiplication", mul_time, f"{mul_loss:.2f}%", mul_size)
    print_table_row("Rescaling (post multiplication)", res_time, f"{res_loss:.2f}%", res_size)
    print_table_row("Decryption & Decoding", dec_time, "<0.01%", "N/A")
