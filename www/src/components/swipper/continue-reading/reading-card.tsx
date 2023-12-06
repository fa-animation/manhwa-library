import {
  Box,
  LinkBox,
  LinkOverlay,
  Stack,
  Tooltip,
  Progress,
  useBreakpointValue
} from '@chakra-ui/react'
import Link from 'next/link'
import * as React from 'react'

interface readingProps {
  title?: string
  image: string
  progress_reading: number
}

export const ReadingCard = ({ title, image, progress_reading }: readingProps) => {
  return (
    <LinkBox as={'article'}>
      <Stack>
        <Box position="relative">
          <Box
            flex={0}
            _before={{
              content: "''",
              display: 'block',
              height: '10rem',
              backgroundImage: `linear-gradient(180deg, rgba(23,25,35,0.09007352941176472) 0%, rgba(23,25,35,0.3449754901960784) 35%, rgba(23,25,35,0.6867121848739496) 100%), url(${image}) `,
              backgroundPosition: 'top',
              backgroundSize: 'cover',
              borderRadius: useBreakpointValue({ base: 'md', md: 'xl' })
            }}
          ></Box>
          {/* <TypeBook type={type_book} /> */}
        </Box>
        <Stack>
          <Stack spacing="1">
            <Tooltip hasArrow label={title} bg="gray.300" color="black" w={'fit-content'}>
              <LinkOverlay as={Link} href={'#'}>
                {/* <Text
                  isTruncated
                  fontWeight="medium"
                  color={useColorModeValue('gray.700', 'gray.400')}
                >
                  {title}
                </Text> */}
                <Progress value={progress_reading} rounded={'base'} size={'sm'} />
                {/* <Rating defaultValue={ratting} /> */}
              </LinkOverlay>
            </Tooltip>
          </Stack>
        </Stack>
      </Stack>
    </LinkBox>
  )
}
