import { Icon, IconProps } from '@chakra-ui/react'
import { IconType } from 'react-icons'

type PropsIcon = IconProps & {
  icon?: IconType
}

const IconCard = ({ icon, ...rest }: PropsIcon) => (
  <Icon rounded="full" w="12" h="12" bg="purple.500" as={icon} {...rest} />
)

export default IconCard
