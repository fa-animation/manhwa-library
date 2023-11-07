import { Box, Heading } from '@chakra-ui/react'
import { Swiper, SwiperSlide } from 'swiper/react'
import 'swiper/css'
import React, { CSSProperties } from 'react'
import { sliderSettings } from '../config'
import { SwiperNavButtons } from '../swiper-nav-buttons'
import { ReadingCard } from './reading-card'
// import PosterCard from './PosterCard'

export interface readingProps {
  title: string
  image: string
  progress_reading: number
}

interface SwipperSliderProps {
  title?: string
}

const slideStyles: CSSProperties = {
  boxSizing: 'border-box',
  maxWidth: '200px'
}

const dataReading: readingProps[] = [
  {
    title: 'A Returner\'s Magic Should Be Special',
    image: 'https://media.kitsu.io/manga/poster_images/54173/original.jpg',
    progress_reading: Math.round(Math.random() * 100)
  },
  {
    title: 'Martial Peak',
    image: 'https://media.kitsu.io/manga/poster_images/40987/original.jpg',
    progress_reading: Math.round(Math.random() * 100)
  },
  {
    title: 'Solo Max-Level Newbie',
    image: 'https://media.kitsu.io/manga/60628/poster_image/d6f918e6b16b3e88330c1829e786be85.jpg',
    progress_reading: Math.round(Math.random() * 100)
  }
]
export const ContinueReading = ({ title }: SwipperSliderProps) => {
  return (
    <Box px={5}>
      <Box w="100%" h="100%">
        <Heading size="md" my="1.5rem" hidden={!title?.length}>
          {title}
        </Heading>
      </Box>
      <Swiper {...sliderSettings} spaceBetween={15}>
        <SwiperNavButtons />
        {dataReading?.map((data: readingProps, i) => (
          <SwiperSlide key={i} style={slideStyles}>
            <ReadingCard
              title={data.title}
              image={data.image}
              progress_reading={data.progress_reading}
            />
          </SwiperSlide>
        ))}
      </Swiper>
    </Box>
  )
}
