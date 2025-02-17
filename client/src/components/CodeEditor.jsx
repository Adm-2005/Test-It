import Editor from '@monaco-editor/react';

export default function CodeEditor({ code, setCode }) {
    

    const handleEditorChange = (event) => {
        setCode(event.target.value);
    }

    return (
        <div className='flex justify-center items-center w-[250px] md:w-[400px] lg:w-[600px]'>
            <Editor 
                height='50vh' 
                width="100%" 
                defaultLanguage='python' 
                theme='hc-black'
                value={code} 
                onChange={handleEditorChange} 
            />
        </div>
    )
}