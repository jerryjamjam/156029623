

//this is a recursive search to a tree
//the first arguement is a pointer to the node tree

bool search(node *tree, int number)
{
    if(tree == NULL)
    {
        return false;
    }
    else if (number < tree->number)
    {
        return search(tree->left, number);
    }
    else if(number > tree->right, number)
    {
        return search(tree->right, number);
    }
    else
    {
        return true;
    }
}
