export interface MangaProps {
  id: string
  title: string
  slug: string
  description: string
  status_progress: string
  ratting: number
  image: string
  view_count: number
  year_published: string
  author: string
  artist: string
  type_book: string
}

export interface MangaT {
  data: MangaProps[]
}

export interface ArrayDataProps {
  lastHomeManga: MangaT
}