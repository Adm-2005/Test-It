import { useState } from "react";
import { IconContext } from "react-icons/lib";
import { MdUploadFile } from "react-icons/md";
import { MdClear } from "react-icons/md";
import { AiOutlineCheckCircle } from "react-icons/ai";

export default function FileUpload({ images, setImages }) {
    const [isDragging, setIsDragging] = useState(false);

    const handleDrop = (event) => {
        event.preventDefault();

        const droppedImages = Array.from(event.dataTransfer.files);

        if (images.length < 4) {
            // e.g. if images already has 3 images only (0, 1) will be sliced from new dropped files
            const newImages = droppedImages.slice(0, 4 - images.length);
            setImages((prevImages) => [...prevImages, ...newImages]);
        }

        setIsDragging(false);
    };

    const handleImageChange = (event) => {
        const selectedImages = Array.from(event.target.files);

        if (images.length < 4) {
            const newImages = selectedImages.slice(0, 4 - images.length);
            setImages((prevImages) => [...prevImages, ...newImages]);
        }
    };

    const handleImageRemoval = (index) => {
        setImages((prevImages) => prevImages.filter((_, i) => i !== index));
    };

    return (
        <div
            onDragEnter={() => setIsDragging(true)}
            onDragOver={(event) => event.preventDefault()}
            onDrop={handleDrop}
            className={
                isDragging
                    ? "w-[250px] md:w-[400px] h-[250px] lg:mt-6 bg-purple-200 border border-purple-950 flex flex-col items-center justify-center rounded-xl"
                    : "w-[250px] md:w-[400px] h-[250px] lg:mt-6 border border-purple-950 flex flex-col items-center justify-center rounded-xl"
            }
        >
            <IconContext.Provider value={{ size: "35px", color: "purple" }}>
                <MdUploadFile />
            </IconContext.Provider>
            <p className="text-slate-600">
                Supported files: .jpg, .jpeg, .png{" "}
            </p>
            {images.length >= 4 ? (
                <p className="text-md text-red-600">File Limit Reached.</p> // no upload option once limit is reached.
            ) : (
                <div className="m-3">
                    <input
                        hidden
                        id="browse"
                        type="file"
                        onChange={handleImageChange}
                        className="relative top-3 w-[105px]"
                        accept=".jpg, .jpeg, .png"
                        multiple
                    ></input>
                    <label
                        htmlFor="browse"
                        className="mt-4 bg-purple-800 hover:bg-purple-950 text-white p-2 font-poppins rounded-xl"
                    >
                        Upload Files
                    </label>
                </div>
            )}

            {images.length > 0 && (
                <div
                    className={
                        images.length > 2
                            ? "m-1 grid grid-rows-2 grid-cols-2 overflow-hidden gap-1"
                            : "m-1 mx-auto grid grid-rows-1 grid-cols-2 overflow-hidden gap-1"
                    }
                >
                    {images.map((image, index) => (
                        <div
                            className="flex justify-between items-center gap-1 bg-slate-400 p-[2px] rounded-md"
                            key={index}
                        >
                            <div className="flex h-full relative bottom-[2px] items-center">
                                <p className="text-sm text-white overflow-hidden whitespace-nowrap max-w-[90px]">
                                    {image.name}
                                </p>
                            </div>
                            <IconContext.Provider
                                value={{ size: "15px", color: "#ffffff" }}
                            >
                                <MdClear
                                    onClick={() => handleImageRemoval(index)}
                                />
                            </IconContext.Provider>
                        </div>
                    ))}
                </div>
            )}

            {images.length > 0 && (
                <span className="flex justify-center items-center gap-1 mt-2">
                    <IconContext.Provider
                        value={{ size: "20px", color: "green" }}
                    >
                        <AiOutlineCheckCircle />
                    </IconContext.Provider>
                    <p className="text-slate-600 text-sm">
                        {images.length}/4 image(s) selected
                    </p>
                </span>
            )}
        </div>
    );
}
