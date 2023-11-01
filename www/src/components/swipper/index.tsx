import { Box, Heading } from '@chakra-ui/react'
import { Swiper, SwiperSlide } from 'swiper/react'
import 'swiper/css'
import React, { CSSProperties } from 'react'
import { MangaProps } from '@/types'
// import PosterCard from './PosterCard'
import { sliderSettings } from './config'
import { SwiperNavButtons } from './swiper-nav-buttons'
import { Card } from '../card-manga/index'

interface SwipperSliderProps {
  section: MangaProps[]
  title?: string
}

const slideStyles: CSSProperties = {
  boxSizing: 'border-box',
  maxWidth: '200px'
}

export const SwipperSlider = ({ section, title }: SwipperSliderProps) => {
  return (
    <Box px={5}>
      <Box w="100%" h="100%">
        <Heading size="md" my="1.5rem" hidden={!title?.length}>
          {title}
        </Heading>
      </Box>
      <Swiper {...sliderSettings} spaceBetween={15}>
        <SwiperNavButtons />
        {section?.map((data: MangaProps) => (
          <SwiperSlide key={data.id} style={slideStyles}>
            <Card
              image={data.image}
              ratting={data.ratting}
              slug={data.slug}
              title={data.title}
              type_book={data.type_book}
            />
          </SwiperSlide>
        ))}
      </Swiper>
    </Box>
  )
}
