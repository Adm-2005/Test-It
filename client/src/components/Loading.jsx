import { IconContext } from "react-icons/lib";
import { ImSpinner6 } from "react-icons/im";

export default function Loading() {
    return (
        <div className="flex justify-center items-center gap-2">
            <IconContext.Provider value={{ size: '40px', color: '#3b0764', className:'animate-spin' }}>
                <ImSpinner6 />
            </IconContext.Provider>
            Loading your content...
        </div>
    )
}