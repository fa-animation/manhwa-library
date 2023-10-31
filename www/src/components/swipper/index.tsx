import { Box, Heading } from '@chakra-ui/react'
import { Swiper, SwiperSlide } from 'swiper/react'
import 'swiper/css'
import React, { CSSProperties } from 'react'
import { MangaProps } from '@/types'
import PosterCard from './PosterCard'
import { sliderSettings } from './config'
import { SwiperNavButtons } from './SwiperNavButtons'

interface SwipperSliderProps {
  section: MangaProps[]
  title: string
}

const slideStyles: CSSProperties = {
  boxSizing: 'border-box',
  maxWidth: '200px'
}

export const SwipperSlider = ({ section, title }: SwipperSliderProps) => {
  return (
    <Box px={5}>
      <Box w="100%" h="100%">
        <Heading size="md" my="1.5rem">
          {title}
        </Heading>
      </Box>
      <Swiper {...sliderSettings} style={{ width: '100%', height: '100%' }}>
        <SwiperNavButtons />
        {section?.map((data: MangaProps) => (
          <SwiperSlide key={data.id} style={slideStyles}>
            <PosterCard slug={data.slug} name={data.title} imageUrl={data.image} />
          </SwiperSlide>
        ))}
      </Swiper>
    </Box>
  )
}
