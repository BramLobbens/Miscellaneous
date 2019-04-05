import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Quicksort {

    public static List<Integer> quicksort(List<Integer> list) {

        if (list.isEmpty()) {
            return list;
        }

        int pivot = list.remove(0);

        List<Integer> output = new ArrayList<>();
        List<Integer> lesserOrEqual = new ArrayList<>();
        List<Integer> greaterThan = new ArrayList<>();

        /*
        for (int val : list) {
            if (val <= pivot) {
                lesserOrEqual.add(val);
            }
            else {
                greaterThan.add(val);
            }
        }
        */
        for (int val : list) {
            List<Integer> target = (val <= pivot) ? lesserOrEqual : greaterThan;
            target.add(val);
        }

        output.addAll(quicksort(lesserOrEqual));
        output.add(pivot);
        output.addAll(quicksort(greaterThan));
        return output;
    }
    
    public static void main(String[] args) {

        List<Integer> vals = new ArrayList(Arrays.asList(5, 1, 9, 7, 6, 3, 2));
        System.out.println(vals);
        System.out.println(quicksort(vals));
    }
}
