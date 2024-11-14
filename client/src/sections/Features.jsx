import Carousel from '../components/Carousel.jsx';
import { featureGroups } from '../utils.jsx';

export default function Features() {
    return (
        <section id='features' className='w-full flex flex-col gap-[30px] p-3 justify-center items-center py-[40px]'>
            <div className='flex flex-col gap-2'>
                <h1 className='font-josefin  font-bold text-center text-purple-950 text-4xl md:text-5xl'>
                    Features
                </h1>
                <p className='text-center text-slate-500 font-poppins italic'>Discover what makes Test-It! your go-to testing tool.</p>
            </div>

            {/* sm screens */}
            <Carousel
                itemsPerSlide={2}
                slideStyle='flex flex-col gap-2'
                controlStyle=''
                paginationStyle=''
                autoPlay={true}
                infinite={true}
                pagination={true}
                controls={false}
                className='md:hidden'
            >
                {
                    featureGroups.map((group, index) => (
                    <div key={index} className='flex justify-center items-center shadow-md border border-slate-100 rounded-sm p-4 h-full'>
                        <div className='w-full h-full flex flex-col justify-center'>
                            <h3 className='font-josefin font-bold text-xl text-purple-950'>{group.name}</h3>
                            <p className='font-poppins font-medium text-slate-600'>{group.text}</p>
                        </div>
                    </div>
                    ))
                }
            </Carousel>

            {/* md screens and larger */}
            <div className='hidden md:grid grid-rows-2 grid-cols-1 md:grid-rows-3 md:grid-cols-2 gap-2 w-[60vw] h-full justify-center items-center'>
                {
                    featureGroups.map((group, index) => (
                    <div key={index} className='flex justify-center items-center shadow-md border border-slate-100 rounded-sm p-4 h-full'>
                        <div className='w-full h-full flex flex-col justify-center'>
                            <h3 className='font-josefin font-bold text-xl text-purple-950'>{group.name}</h3>
                            <p className='font-poppins font-medium text-slate-600'>{group.text}</p>
                        </div>
                    </div>
                    ))
                }
            </div>
        </section>
    )
}