/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int integerLength(int num)
{
    int count = 0;
    while (num != 0)
    {
        num /= 10;
        count++;
    }
    return count;
}

void initializeArr(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        arr[i] = 0;
    }
}

int integerArrToInteger(int arr[], int size)
{
    int integer = 0;
    for(int i = 0; i < size; i++)
    {
        integer += arr[size - 1 - i] * pow(10, i);
    }

    return integer;
}

void integerToIntegerArr(int arr[], int size, int integer)
{
    for(int i = 0; i < size; i++)
    {
        arr[size - 1 - i] = integer % 10;
        integer /= 10;
    }
}

int *addToArrayForm(int *num, int numSize, int k, int *returnSize)
{

    if (numSize >= integerLength(k))
    {
        int interArrSize = 0;
        if (numSize <= 4)
        {
            interArrSize = 5;
        }
        else
        {
            interArrSize = numSize + 1;
        }

        int interArr[interArrSize];
        initializeArr(interArr, interArrSize);

        int kSize = integerLength(k);
        int carry = 0;
        int rightDigit = 0;
        int rightArrDigit = 0;
        int sum = 0;

        int i;
        for (i = 0; i < kSize; i++)
        {
            rightDigit = k % 10;
            k /= 10;

            rightArrDigit = num[numSize - 1 - i];

            sum = rightDigit + rightArrDigit + carry;

            if (integerLength(sum) == 1)
            {
                interArr[interArrSize - 1 - i] = sum;
                carry = 0;
            }
            else
            {
                interArr[interArrSize - 1 - i] = (sum % 10);
                carry = sum / 10;
            }
        }

        for (; i < numSize; i++)
        {
            sum = num[numSize - 1 - i] + carry;

            if (integerLength(sum) == 1)
            {
                interArr[interArrSize - 1 - i] = sum;
                carry = 0;
            }
            else
            {
                interArr[interArrSize - 1 - i] = (sum % 10);
                carry = sum / 10;
            }
        }

        interArr[interArrSize - 1 - i] = carry;

        i = 0;
        int extraSpace = 0;
        while (interArr[i] == 0)
        {
            i++;
        }

        extraSpace = i;

        int finalArrSize = interArrSize - extraSpace;
        int *finalArr = (int *)malloc(finalArrSize * sizeof(int));

        i = extraSpace;
        int j = 0;
        while (j < finalArrSize)
        {
            finalArr[j] = interArr[i];
            i++;
            j++;
        }

        *returnSize = finalArrSize;
        return finalArr;
    }
    else
    {
        int givenInt = integerArrToInteger(num, numSize);
        givenInt += k;

        int finalArrSize = integerLength(givenInt);
        int *finalArr = (int*)malloc(finalArrSize * sizeof(int));

        integerToIntegerArr(finalArr, finalArrSize, givenInt);
        *returnSize = finalArrSize;
        return finalArr;
    }
}

void main()
{
    int numSize = 1;
    int num[] = {1};
    int k = 1000;
    int returnSize = 0;

    int *outArr = addToArrayForm(num, numSize, k, &returnSize);

    for (int i = 0; i < returnSize; i++)
    {
        printf("%d", outArr[i]);
    }
}