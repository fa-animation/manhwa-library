import { extendTheme } from '@chakra-ui/react'
import { config } from './foundations/config'
import { fonts, fontWeights, fontSizes } from './foundations/fonts'
import { radii } from './foundations/radii'
import { styles } from './foundations/styles'

const customTheme = extendTheme({
  radii,
  fonts,
  fontWeights,
  fontSizes,
  config,
  styles
})

export default customTheme
