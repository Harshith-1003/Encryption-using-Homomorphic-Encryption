import tenseal as ts

# Step 1: Create TenSEAL context with CKKS scheme
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.global_scale = 2**40
context.generate_galois_keys()  # For rotation and other operations

# Step 2: Prepare data
plain_vector1 = [1.0, 2.0, 3.0]
plain_vector2 = [4.0, 5.0, 6.0]

# Step 3: Encrypt vectors using CKKS
enc_vector1 = ts.ckks_vector(context, plain_vector1)
enc_vector2 = ts.ckks_vector(context, plain_vector2)

# Step 4: Perform homomorphic operations
enc_sum = enc_vector1 + enc_vector2           # Homomorphic addition
enc_product = enc_vector1 * enc_vector2       # Homomorphic multiplication (element-wise)

# Step 5: Decrypt results
dec_sum = enc_sum.decrypt()
dec_product = enc_product.decrypt()

# Step 6: Print results
print("Decrypted Sum: ", dec_sum)
print("Decrypted Product: ", dec_product)