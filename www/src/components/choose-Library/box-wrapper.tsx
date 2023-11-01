import { Box } from '@chakra-ui/react'
import { BoxProps } from '@chakra-ui/layout'

interface Props extends BoxProps {
  children: React.ReactNode
}

export const BoxWrapper = ({ children, ...props }: Props) => (
  <Box pos="relative" rounded="12px" shadow="base" p="40px" {...props}>
    {children}
  </Box>
)
