import { Box } from '@chakra-ui/react'
import { BoxProps } from '@chakra-ui/layout'

interface Props extends BoxProps {
  children: React.ReactNode
}

export const Section = ({ children, ...props }: Props) => (
  <Box
    as={'section'}
    bg={'purple.600'}
    bgImage={'/svg/blob.svg'}
    bgPosition={'bottom center'}
    bgRepeat={'space no-repeat'}
    bgSize={'120px'}
    {...props}
  >
    {children}
  </Box>
)
