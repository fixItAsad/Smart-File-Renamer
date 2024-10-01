import os 
import streamlit as st
import time
st.title("Smart Files Renamer🧹")
def file_renamer():
    try:
        input_to_file = {"1.Txt File 🏵️":".txt",
                    "2.Png File 🍀":".png",
                    "3.Jpg file 🌟":".jpg",
                    "4.Pdf file ☘️":".pdf",
                    "5.Jpeg  file 🌸":".jpeg",
                    "6.PNG file 🎀":".PNG"}
        print()
        format_for_user = ("1.Txt File 🏵️","2.Png File 🍀","3.Jpg file 🌟","4.Pdf file ☘️","5.Jpeg  file 🌸","6.PNG file 🎀")
        file_user_input = st.radio("Which type of file you need to rename 📂:",format_for_user,key="Radio key")
        dict_path = st.text_input("╰┈➤ Please enter the path of Folder i.e C:\\User\\XYZ\\Documents: ",key="Directory path")
        summit_button = st.button(label="Rename Now!")
        if summit_button:
            if os.path.exists(dict_path):
                dict_path.replace("\\","/")
                renamed_count = 0
                unique_count = 0
                final_File_format = input_to_file[file_user_input]
                list_direcoterios = os.listdir(dict_path)
                file_found = False
                for file in list_direcoterios:
                    if file.endswith(final_File_format):
                        file_found = True
                        unique_count += 1
                        new_file_name =  f"{unique_count}.{final_File_format}"
                        new_name = os.path.join(dict_path,new_file_name)
                        old_name = os.path.join(dict_path,file)
                        count = 0

                        while os.path.exists(new_name):
                            new_file_name =  f"{unique_count}.{count}{final_File_format}"
                            new_name = os.path.join(dict_path,new_file_name)
                            old_name = os.path.join(dict_path,file)
                            count += 1
                        try:
                            os.rename(old_name,new_name)
                            renamed_count +=1 
                        except Exception as error:
                            st.error(f"SomeThing Went Wrong, error is {error}")
                if not file_found:
                    st.error("No Entered format file(s) were found!")
                if file_found:
                    my_progress = st.progress(0)
                    for i in range(0,101):
                        time.sleep(0.1)
                        my_progress.progress(i,text="Progress...")
                    st.balloons()
                    st.success(f"{renamed_count} files(s) were Renamed Succeffuly!")
                    st.info("Note: Please refresh the Files folder if files have not been renamed!")
            else:
                st.error("No Such Directory Were Found!")
    except Exception as e:
        st.exception(f"Something went Wrong error is: {e}")
    print()
    st.caption("This Tool is Developed by Muhammad Asad ❤️")
if __name__ == "__main__":                    
    file_renamer()