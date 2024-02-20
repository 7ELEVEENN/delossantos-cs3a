import streamlit as st

st.header("Caesar Cipher")

text = st.text_input("Text:")
shift_keys = list(map(int, st.text_input("Shift Keys:").split()))


if st.button("Submit"):

    def encrypt_decrypt(text, shift_keys, ifdecrypt):
        """
        Encrypts a text using Caesar Cipher with a list of shift keys.
        Args:
            text: The text to encrypt.
            shift_keys: A list of integers representing the shift values for each character.
            ifdecrypt: flag if decrypt or encrypt
        Returns:
            A string containing the encrypted text if encrypt and plain text if decrypt
        """
        result = ""
        # Constraint
        assert 1 < len(shift_keys) <= len(text), "Length of shift keys is invalid"
        
        for i, char in enumerate(text):
            shift = shift_keys[i % len(shift_keys)]
            # Constraint: character accepted range 
            if 32 <= ord(char) <= 125:
                if ifdecrypt:
                    asc = ord(char) - shift
                else:
                    asc = ord(char) + shift

                while asc > 125:
                    asc -= 94
                while asc < 32:
                    asc += 94
                
                result += chr(asc)
                
            else:
                result+=char
            # st.write(i, char, shift, result[i])
        return result

    # Example usage
    st.write("")
    enc = encrypt_decrypt(text, shift_keys, False)
    st.write("-"*10)
    dec = encrypt_decrypt(enc, shift_keys, True)
    st.write("-"*10)
    st.write("\nText:", text)
    st.write("Shift keys:", *shift_keys)
    st.write("Cipher:", enc)
    st.write("Decrypted text:", dec)
    st.balloons()

