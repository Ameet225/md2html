from md2html.converter import md_to_html
import argparse

def run():
    
    parser = argparse.ArgumentParser(description = "Convert markdown to html")
    parser.add_argument("--input","-i",help= "Enter the input mardown file", required= True)
    parser.add_argument("--output","-o",help= "Enter the output HTML file required", required= True)
    args = parser.parse_args()
    
    fname = args.input
    

    with open(fname,'r',encoding= 'utf-8') as ifile:
        text = ifile.read()

    html_input = md_to_html(text)

    output_path = args.output

    with open(output_path,'w',encoding= 'utf-8') as ofile:
        ofile.write(html_input)
        


    print(f"Mardown file: {args.input} successfully converted to: {args.output}")

if __name__ == "__main__":
    run()
