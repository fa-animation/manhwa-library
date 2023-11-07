import { Box, Heading } from '@chakra-ui/react'
import { Swiper, SwiperSlide } from 'swiper/react'
import 'swiper/css'
import React, { CSSProperties } from 'react'
import { sliderSettings } from '../config'
import { SwiperNavButtons } from '../swiper-nav-buttons'
import { ReadingCard } from './reading-card'
import { MangaProps } from '@/types'
// import PosterCard from './PosterCard'

interface SwipperSliderProps {
  title?: string
  section: MangaProps[]
  progress_reading: number
}

const slideStyles: CSSProperties = {
  boxSizing: 'border-box',
  maxWidth: '200px'
}

export const ContinueReading = ({ title, section, progress_reading }: SwipperSliderProps) => {
  return (
    <Box px={5} hidden={!section.length}>
      <Box w="100%" h="100%">
        <Heading size="md" my="1.5rem" hidden={!title?.length}>
          {title}
        </Heading>
      </Box>
      <Swiper {...sliderSettings} spaceBetween={15}>
        <SwiperNavButtons />
        {section?.map((data: MangaProps, i) => (
          <SwiperSlide key={i} style={slideStyles}>
            <ReadingCard
              title={data.title}
              image={data.image}
              progress_reading={progress_reading}
            />
          </SwiperSlide>
        ))}
      </Swiper>
    </Box>
  )
}
