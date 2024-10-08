# Висновки щодо ефективності алгоритмів сортування

## Опис алгоритмів
- **Insertion Sort**: Алгоритм сортування вставками. Ефективний для малих наборів даних або частково відсортованих масивів. Має квадратичну складність O(n^2) у гіршому випадку.
- **Merge Sort**: Алгоритм сортування злиттям. Має складність O(n log n) у всіх випадках і є ефективним навіть для великих наборів даних.

## Результати вимірювань

### Розмір даних: 10
- **Random data**:
  - Insertion Sort: 0.000006 seconds
  - Merge Sort: 0.000013 seconds
- **Sorted data**:
  - Insertion Sort: 0.000002 seconds
  - Merge Sort: 0.000012 seconds
- **Reversed data**:
  - Insertion Sort: 0.000004 seconds
  - Merge Sort: 0.000007 seconds

### Розмір даних: 100
- **Random data**:
  - Insertion Sort: 0.000123 seconds
  - Merge Sort: 0.000093 seconds
- **Sorted data**:
  - Insertion Sort: 0.000008 seconds
  - Merge Sort: 0.000079 seconds
- **Reversed data**:
  - Insertion Sort: 0.000330 seconds
  - Merge Sort: 0.000083 seconds

### Розмір даних: 1000
- **Random data**:
  - Insertion Sort: 0.016875 seconds
  - Merge Sort: 0.001286 seconds
- **Sorted data**:
  - Insertion Sort: 0.000082 seconds
  - Merge Sort: 0.001041 seconds
- **Reversed data**:
  - Insertion Sort: 0.032029 seconds
  - Merge Sort: 0.001053 seconds

## Загальні висновки
- **Insertion Sort** працює добре для малих наборів даних та відсортованих масивів, але погано справляється з великими та реверсованими даними.
- **Merge Sort** є стабільним алгоритмом, який показує хорошу продуктивність на всіх типах наборів даних незалежно від їх стану (випадкові, відсортовані, реверсовані).
"""